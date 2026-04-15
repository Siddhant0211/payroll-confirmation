frappe.ui.form.on("*", {
    after_save(frm) {

        if (frm.doc.docstatus !== 1) return;

        let meta = frappe.get_meta(frm.doc.doctype);
        if (meta.module !== "Payroll") return;

        if (!meta.is_submittable) return;

        if (frm.__redirected) return;
        frm.__redirected = true;

        let docname = frm.doc.name;
        let doctype = frm.doc.doctype;


        frappe.set_route("hrms_confirmation",docname,(slugify(doctype)));
    }
});

function slugify(text) {
    return text.toLowerCase().replace(/\s+/g, '-');
}