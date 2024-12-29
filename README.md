# SHA256-Learning
Repo to learn about SHA256


# Python Environment Setup

## Prerequisites
1. **Install Python**: Download from [python.org](https://www.python.org/downloads/).  
   Verify installation:
   ```bash
   python --version
   ```

2. **Install `venv`**: Included in Python 3.3+ or install via your package manager:
   ```bash
   sudo apt-get install python3-venv  # For Linux
   ```

## Steps to Create and Use a Virtual Environment

1. **Create Environment**:  
   ```bash
   python -m venv env
   ```

2. **Activate Environment**:  
   - **Windows**: `.\env\Scripts\activate`  
   - **Mac/Linux**: `source env/bin/activate`

3. **Install Dependencies**:  
   ```bash
   pip install <package-name>
   ```

4. **Save Installed Packages**:  
   ```bash
   pip freeze > requirements.txt
   ```

5. **Deactivate Environment**:  
   ```bash
   deactivate
   ```

## Notes
- Reactivate the environment with the same activation command.
- Use `requirements.txt` to recreate environments:
  ```bash
  pip install -r requirements.txt
  ```

--- 

Let me know if you'd like further refinements!