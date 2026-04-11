# Environment Setup (Requirements)

To ensure the scripts run smoothly across different environments (Windows, Mac, Google Colab), students should install the following:

```bash
pip install pandas requests pydantic
```

## Special Note for "Vibe Coders":
If you are using **Google Colab**, you can use this cell at the top:
```python
!pip install pandas requests pydantic
```

## Data Access:
Ensure `raw_data.json` is in the same directory as your script. Use `os.path.join` for file paths if you are on Windows.
