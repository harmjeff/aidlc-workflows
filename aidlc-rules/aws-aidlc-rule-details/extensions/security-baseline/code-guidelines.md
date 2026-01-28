## Security Baseline - Code Generation Guidelines

**Extension**: security-baseline v1.0.0
**Applies To**: Code Generation Stage

---

### Mandatory Secure Coding Requirements

#### 1. Linter Configuration

**Every project MUST include appropriate linting with security rules:**

##### JavaScript/TypeScript
```json
// .eslintrc.json or eslint.config.js
{
  "plugins": ["security"],
  "extends": ["plugin:security/recommended"],
  "rules": {
    "security/detect-object-injection": "error",
    "security/detect-non-literal-regexp": "warn",
    "security/detect-unsafe-regex": "error",
    "security/detect-buffer-noassert": "error",
    "security/detect-eval-with-expression": "error",
    "security/detect-no-csrf-before-method-override": "error",
    "security/detect-possible-timing-attacks": "warn"
  }
}
```

##### Python
```toml
# pyproject.toml - Ruff configuration
[tool.ruff]
select = [
  "S",    # flake8-bandit (security)
  "B",    # flake8-bugbear
  "A",    # flake8-builtins
  "C4",   # flake8-comprehensions
]

[tool.bandit]
exclude_dirs = ["tests", "venv"]
skips = []
```

##### Java
```xml
<!-- pom.xml - SpotBugs with FindSecBugs -->
<plugin>
  <groupId>com.github.spotbugs</groupId>
  <artifactId>spotbugs-maven-plugin</artifactId>
  <configuration>
    <plugins>
      <plugin>
        <groupId>com.h3xstream.findsecbugs</groupId>
        <artifactId>findsecbugs-plugin</artifactId>
      </plugin>
    </plugins>
  </configuration>
</plugin>
```

##### Go
```yaml
# .golangci.yml
linters:
  enable:
    - gosec
    - staticcheck
    - govet
    - errcheck
```

---

### Secure Coding Patterns

#### Input Validation

```python
# ✅ CORRECT: Validate and sanitize input
from pydantic import BaseModel, validator

class UserInput(BaseModel):
    username: str
    email: str
    
    @validator('username')
    def validate_username(cls, v):
        if not v.isalnum():
            raise ValueError('Username must be alphanumeric')
        if len(v) > 50:
            raise ValueError('Username too long')
        return v
```

```typescript
// ✅ CORRECT: Use schema validation
import { z } from 'zod';

const UserSchema = z.object({
  username: z.string().regex(/^[a-zA-Z0-9]+$/).max(50),
  email: z.string().email(),
});

function processUser(input: unknown) {
  const user = UserSchema.parse(input); // Throws on invalid
  // ... use validated user
}
```

#### Parameterized Queries

```python
# ✅ CORRECT: Parameterized query
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# ❌ WRONG: String interpolation
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
```

```java
// ✅ CORRECT: Prepared statement
PreparedStatement stmt = conn.prepareStatement(
    "SELECT * FROM users WHERE id = ?"
);
stmt.setInt(1, userId);

// ❌ WRONG: String concatenation
Statement stmt = conn.createStatement();
stmt.executeQuery("SELECT * FROM users WHERE id = " + userId);
```

#### Secrets Management

```python
# ✅ CORRECT: Environment variables
import os
api_key = os.environ.get('API_KEY')

# ✅ CORRECT: AWS Secrets Manager
import boto3
client = boto3.client('secretsmanager')
secret = client.get_secret_value(SecretId='my-secret')

# ❌ WRONG: Hardcoded secrets
api_key = "sk-1234567890abcdef"
```

#### Error Handling

```python
# ✅ CORRECT: Generic user error, detailed logging
import logging
logger = logging.getLogger(__name__)

try:
    result = process_payment(data)
except PaymentError as e:
    logger.error(f"Payment failed: {e}", exc_info=True)
    raise HTTPException(status_code=400, detail="Payment processing failed")

# ❌ WRONG: Exposing internal details
except Exception as e:
    return {"error": str(e), "stack": traceback.format_exc()}
```

---

### Code Generation Checklist

Before generating code, ensure:

- [ ] Linter configuration file included with security rules
- [ ] Input validation on all external data entry points
- [ ] Parameterized queries for all database operations
- [ ] No hardcoded secrets (use environment variables or secret managers)
- [ ] Generic error messages for users, detailed internal logging
- [ ] HTTPS/TLS for all external communications
- [ ] Proper encoding for output (HTML encoding, JSON encoding, etc.)

---

*This content is provided by the security-baseline extension.*