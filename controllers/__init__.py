from .EmployeeController import employee_bp
from .LoginController import login_bp
from .UsersController import users_bp
from .TaskJournalController import task_journal_bp
# Список всех blueprints
blueprints = [employee_bp, login_bp, users_bp, task_journal_bp]