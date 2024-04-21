import json
import frappe


def execute():
    """"Add "Pioneers"'s Workspace"""
    print(f"Patch: _2024_4_20_create_pioneers_workspace started")
    _add_lava_cms_basic_workspace()
    print(f"Patch: _2024_4_20_create_pioneers_workspace finished")


def _add_lava_cms_basic_workspace():
    workspace_title = "Pioneers"    # will be used as its ID as well
    if frappe.db.exists("Workspace", workspace_title):
        print(f"Workspace {workspace_title} already exists")
    else:
        shortcuts = [
            {
                "doc_view": "List",
                "label": "Students",
                "link_to": "Students",
                "doctype": "DocType"
            },
            {
                "doc_view": "List",
                "label": "Parents",
                "link_to": "Parents",
                "doctype": "DocType"
            },
            {
                "doc_view": "List",
                "label": "Universities",
                "link_to": "Universities",
                "doctype": "DocType"
            },
            {
                "doc_view": "List",
                "label": "Majors",
                "link_to": "Majors",
                "doctype": "DocType"
            },
            {
                "doc_view": "List",
                "label": "Accommodation",
                "link_to": "Accommodation",
                "doctype": "DocType"
            },
        ]
        roles = [
            {
                "role": "System Manager"
            }
        ]

        try:
            content = []
            workspace_doc = frappe.new_doc("Workspace")
            workspace_doc.name = workspace_title
            workspace_doc.label = workspace_title
            workspace_doc.title = workspace_title
            workspace_doc.sequence_id = 1
            workspace_doc.public = 1
            workspace_doc.is_standard = 1
            workspace_doc.module = "Pioneers App"
            for shortcut in shortcuts:
                workspace_doc.append("shortcuts", {
                    "doctype": shortcut["doctype"],
                    "label": shortcut["label"],
                    "link_to": shortcut["link_to"],
                    "doc_view": shortcut["doc_view"]
                })
                content.append({"type": "shortcut", "data": {"shortcut_name": shortcut["label"], "col": 4}})
            for role in roles:
                workspace_doc.append("roles", {
                    "role": role["role"]
                })

            workspace_doc.content = json.dumps(content)
            workspace_doc.insert(ignore_permissions=True)
            print(f"Workspace {workspace_title} added successfully")
        except Exception as e:
            print(f"Error adding Workspace {workspace_title}: {e}")