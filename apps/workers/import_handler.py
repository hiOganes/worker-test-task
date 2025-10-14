import openpyxl
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Worker


def import_workers_from_excel(file, user):
    wb = openpyxl.load_workbook(file)
    ws = wb.active
    added = 0
    errors = []
    
    for row_num, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
        try:
            first_name, middle_name, last_name, email, position = row[:5]
            if not all([first_name, last_name, email, position]):
                raise ValueError("Missing required fields")
            
            validate_email(email)
            if Worker.objects.filter(email=email).exists():
                raise ValueError("Duplicate email")
            
            worker = Worker(
                first_name=first_name,
                middle_name=middle_name or '',
                last_name=last_name,
                email=email,
                position=position,
            )
            worker.full_clean()
            worker.save()
            added += 1
        except Exception as e:
            errors.append({"row": row_num, "error": str(e)})
    
    return {"added": added, "errors": errors}