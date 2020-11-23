# Blockchain for a cryptocurrency from scratch using Python.

---

## **Set up a venv:**

1. create the venv:
```bash
python3 -m venv <env-name>
```

2. activate the env:
```bash
source <env-name>/bin/activate
```

3. show which env you are using atm (optional):
```bash
echo $VIRTUAL_ENV
```

**Install all packages**
```bash
pip3 install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```bash
python3 -m pytest backend/tests
```


**Run the application and API**

Make sure to activate the virtual environment.

```bash
python3 -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```bash
export PEER=True && python3 -m backend.app
```
