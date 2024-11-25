from .EmployeeController import employee_bp
from .LoginController import login_bp
from .UsersController import users_bp
from .TaskJournalController import task_journal_bp
from .ResourcesController import resources_bp
from .MissionController import missions_bp
from .ReportsJournalController import reports_journal_bp
from .ExperimentJournalController import experiment_journal_bp
from .CompletedTasksController import completed_tasks_bp
# Список всех blueprints
blueprints = [employee_bp, login_bp, users_bp, task_journal_bp, resources_bp, missions_bp, reports_journal_bp, experiment_journal_bp, completed_tasks_bp]