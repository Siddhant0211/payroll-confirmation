app_name = "payroll_confirmation"
app_title = "Payroll Confirmation"
app_publisher = "siddhant"
app_description = "Payroll Confirmation"
app_email = "siddhant.saxena@nexityconsulting.com"
app_license = "agpl-3.0"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "payroll_confirmation",
# 		"logo": "/assets/payroll_confirmation/logo.png",
# 		"title": "Payroll Confirmation",
# 		"route": "/payroll_confirmation",
# 		"has_permission": "payroll_confirmation.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/payroll_confirmation/css/payroll_confirmation.css"
# app_include_js = "/assets/payroll_confirmation/js/payroll_confirmation.js"

# include js, css files in header of web template
# web_include_css = "/assets/payroll_confirmation/css/payroll_confirmation.css"
# web_include_js = "/assets/payroll_confirmation/js/payroll_confirmation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "payroll_confirmation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "payroll_confirmation/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "payroll_confirmation.utils.jinja_methods",
# 	"filters": "payroll_confirmation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "payroll_confirmation.install.before_install"
# after_install = "payroll_confirmation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "payroll_confirmation.uninstall.before_uninstall"
# after_uninstall = "payroll_confirmation.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "payroll_confirmation.utils.before_app_install"
# after_app_install = "payroll_confirmation.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "payroll_confirmation.utils.before_app_uninstall"
# after_app_uninstall = "payroll_confirmation.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "payroll_confirmation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"payroll_confirmation.tasks.all"
# 	],
# 	"daily": [
# 		"payroll_confirmation.tasks.daily"
# 	],
# 	"hourly": [
# 		"payroll_confirmation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"payroll_confirmation.tasks.weekly"
# 	],
# 	"monthly": [
# 		"payroll_confirmation.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "payroll_confirmation.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "payroll_confirmation.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "payroll_confirmation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "payroll_confirmation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["payroll_confirmation.utils.before_request"]
# after_request = ["payroll_confirmation.utils.after_request"]

# Job Events
# ----------
# before_job = ["payroll_confirmation.utils.before_job"]
# after_job = ["payroll_confirmation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"payroll_confirmation.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# Require all whitelisted methods to have type annotations
require_type_annotated_api_methods = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

