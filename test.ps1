. .\.venv\Scripts\Activate.ps1

python -m pytest test_visualisation.py

$PYTEST_EXIT_CODE = $?

if ($PYTEST_EXIT_CODE -eq 0) {
    exit 0
} else {
    exit 1
}
