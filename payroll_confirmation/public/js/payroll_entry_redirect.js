frappe.provide("erpnext.payroll");
erpnext.payroll.submit_salary_slip = function (frm) {
    frappe.confirm(
        __(
            "This will submit Salary Slips and create accrual Journal Entry. Do you want to proceed?"
        ),
        function () {
            frappe.call({
                method: "submit_salary_slips",
                args: {},
				doc: frm.doc,
				freeze: true,
				freeze_message: __("Submitting Salary Slips and creating Journal Entry..."),
                callback: function (r) {
                    if (r.message && r.message.status === "completed") {
                        frappe.set_route("hrms_confirmation",frm.doc.name,slugify("Payroll Entry"));
                    }

                    if (r.message && r.message.status === "queued") {
                        frappe.show_alert({
                            message: __("Salary slip submission is queued."),
                            indicator: "blue",
                        });
                    }
                },
            });
        }
    );
};

function slugify(text) {
    return text.toLowerCase().replace(/\s+/g, '-');
}