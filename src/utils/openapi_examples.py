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
