frappe.pages['hrms_confirmation'].on_page_show = function(wrapper) {
	wrapper.innerHTML = "";

    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: "HRMS Confirmation",
        single_column: true,
    });

   
 $(page.body).html(`
        <div class="text-center p-5">
            <i class="fa fa-spinner fa-spin fa-2x"></i>
            <p>Loading payroll details...</p>
        </div>
    `);

    const route = frappe.get_route();
    const raw_doctype = route[route.length - 1];
    const docname = decodeURIComponent(route.slice(1, -1).join("/"));

    const doctype = raw_doctype
        .replace(/-/g, " ")
        .replace(/\b\w/g, c => c.toUpperCase());

    if (!docname || !doctype) {
        $(page.body).html("<h3>Invalid payroll confirmation route.</h3>");
        return;
    }

    frappe.call({
        method: "frappe.client.get",
        args: { doctype, name: docname },

        callback: function (r) {
            if (!r.message) {
                $(page.body).html("<h3>Payroll document not found.</h3>");
                return;
            }

            const doc = r.message;

            /* ✅ ONLY AFTER SUBMIT */
            if (doc.docstatus !== 1) {
                $(page.body).html(`
                    <h3>This payroll document is not submitted yet.</h3>
                `);
                return;
            }

            /* ─────────────────────────────
               PAYROLL DETAILS
            ───────────────────────────── */
            const description = `${doctype} has been Successfully Submitted`;

            const company = doc.company || "-";
            const employee = doc.employee_name || doc.employee || "-";

            const posting_date = doc.posting_date
                ? frappe.datetime.str_to_user(doc.posting_date)
                : "-";
            
            
            const period_label = ["Payroll Entry", "Salary Slip"].includes(doctype)
                ? "Monthly Period"
                : "Payroll Period";

            const payroll_period =
                doc.payroll_period ||
                (doc.start_date && doc.end_date
                    ? `${frappe.datetime.str_to_user(doc.start_date)} → ${frappe.datetime.str_to_user(doc.end_date)}`
                    : "-");

            const net_pay =
                doc.net_pay !== undefined
                    ? frappe.format(doc.net_pay, { fieldtype: "Currency" })
                    : "-";

            /* ─────────────────────────────
               FINAL HTML
            ───────────────────────────── */
            const html = `
                <div class="action-buttons">
                    <button class="btn btn-default btn-lg btn-dashboard">
                        <i class="fa fa-th-list"></i> Payroll Dashboard
                    </button>
                    <button class="btn btn-secondary btn-lg btn-view-request">
                        <i class="fa fa-eye"></i> View ${doctype}
                    </button>
                </div>

                <div class="mr-success-container">
                    <div class="success-icon">
                        <svg width="80" height="80" viewBox="0 0 80 80" fill="none">
                        <circle cx="40" cy="40" r="40" fill="#10b981" opacity="0.1"></circle>
                        <circle cx="40" cy="40" r="32" fill="#10b981"></circle>
                        <path d="M26 40L35 49L54 30" stroke="white" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"></path>
                        </svg>
                    </div>

                    <div class="success-header">
                        <h2 class="success-title">${description}</h2>
                    </div>

                    <div class="cards-row">

                        <div class="detail-card full-width">
                            <div class="card-body">

                                <div class="detail-row">
                                    <span>ID:</span>
                                    <a href="/desk/${frappe.router.slug(doctype)}/${encodeURIComponent(docname)}">
                                        ${docname}
                                    </a>
                                </div>

                                <div class="detail-row">
                                    <span>Status:</span>
                                    <span class="badge badge-success">
                                        Submitted
                                    </span>
                                </div>

                                <div class="detail-row">
                                    <span>Employee:</span>
                                    <span>${employee}</span>
                                </div>

                                <div class="detail-row">
                                    <span>${period_label}:</span>
                                    <span>${payroll_period}</span>
                                </div>

                                <div class="detail-row">
                                    <span>Posting Date:</span>
                                    <span>${posting_date}</span>
                                </div>

                                <div class="detail-row">
                                    <span>Net Pay:</span>
                                    <strong>${net_pay}</strong>
                                </div>

                                <div class="detail-row">
                                    <span>Company:</span>
                                    <span>${company}</span>
                                </div>

                            </div>
                        </div>

                    </div>
                </div>
            `;

            $(page.body).html(html);

            /* ─────────────────────────────
               ACTIONS
            ───────────────────────────── */
            $(".btn-dashboard").click(() =>
                frappe.set_route("List", doctype)
            );

            $(".btn-view-request").click(() =>
                frappe.set_route("Form", doctype, docname)
            );
        }
    });
};
