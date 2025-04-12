from datetime import datetime


class ServicesOE:
    post = {
        "1": {
            "summary": "service1",
            "value": {
                "name": "стрижка",
                "description": "модельная стрижка",
                "duration": 30,
                "price": 500,
            },
        },
        "2": {
            "summary": "service2",
            "value": {
                "name": "бритьё",
                "description": "под корень",
                "duration": 15,
                "price": 300,
            },
        },
        "3": {
            "summary": "service3",
            "value": {
                "name": "покраска",
                "description": "покраска волос",
                "duration": 120,
                "price": 3000,
            },
        },
    }


class AuthOE:
    post = {
        "1": {
            "summary": "admin",
            "value": {
                "phone": "+79521111111",
                "telagram": "@admin",
                "role": "admin",
                "name": "Sanek",
                "email": "admin@example.com",
                "password": "111",
            },
        },
        "2": {
            "summary": "barber",
            "value": {
                "phone": "+79523333333",
                "telagram": "@barber",
                "role": "barber",
                "name": "Galya",
                "email": "barber@example.com",
                "password": "222",
            },
        },
        "3": {
            "summary": "client",
            "value": {
                "phone": "+79524444444",
                "telagram": "@client",
                "role": "client",
                "name": "Seroja",
                "email": "client@example.com",
                "password": "333",
            },
        },
    }
    login = {
        "1": {
            "summary": "admin",
            "value": {
                "phone": "+79521111111",
                "password": "111",
            },
        },
        "2": {
            "summary": "barber",
            "value": {
                "phone": "+79523333333",
                "password": "222",
            },
        },
        "3": {
            "summary": "client",
            "value": {
                "phone": "+79524444444",
                "password": "333",
            },
        },
    }


class NotificationsOE:
    post = {
        "1": {
            "summary": "service1",
            "value": {
                "user_id": 15,
                "content": "some content",
                "type": "appointment_reminder_24h",
                "status": "pending",
                "scheduled_at": datetime.strptime("01.11.2025", "%d.%m.%Y"),
                "sent_at": datetime.strptime("02.11.2025", "%d.%m.%Y"),
            },
        },
        "2": {
            "summary": "service2",
            "value": {
                "user_id": 16,
                "content": "some content",
                "type": "appointment_reminder_1h",
                "status": "pending",
                "scheduled_at": datetime.strptime("01.11.2025", "%d.%m.%Y"),
                "sent_at": datetime.strptime("02.11.2025", "%d.%m.%Y"),
            },
        },
        "3": {
            "summary": "service3",
            "value": {
                "user_id": 17,
                "content": "some content",
                "type": "mass_notification",
                "status": "pending",
                "scheduled_at": datetime.strptime("01.11.2025", "%d.%m.%Y"),
                "sent_at": datetime.strptime("02.11.2025", "%d.%m.%Y"),
            },
        },
    }
