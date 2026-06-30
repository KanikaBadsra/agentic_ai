ROLE_PERMISSIONS = {

    "Admin": {
        "sql": True,
        "analytics": True,
        "delete": True
    },

    "Analyst": {
        "sql": True,
        "analytics": True,
        "delete": False
    },

    "Viewer": {
        "sql": False,
        "analytics": True,
        "delete": False
    }
}