const baseURL = '/api'

const auth = '/auth'

const cars = '/cars_ad'

const users = '/users'

const urls = {
    auth:{
        auth: auth,
        refresh: auth + '/refresh',
        activate_user: (token)=> urls.auth.auth + '/activate/' + token,
        recovery_request: auth + '/recovery_request',
        recovery: (token)=> urls.auth.auth + '/recovery/' + token
    },
    cars:{
        cars: cars,
        car_by_id: (id)=> urls.cars.cars + '/' + id,
        create_ad: cars + '/create_ad',
        change_ad: (id)=> urls.cars.cars + '/' + id + '/change_ad',
        add_photos: (id)=> urls.cars.cars + '/' + id + '/add_photos',
        check_censorship: (id)=> urls.cars.cars + '/' + id + '/check_censorship'
    },
    users:{
        register: users,
        list_users: users + '/list',
        ban_user: (id)=> urls.users.register+ '/' + id + '/ban',
        unban_user: (id)=> urls.users.register+ '/' + id + '/unban',
        create_admin_user: (id)=> urls.users.register+ '/' + id + '/create_admin',
        cancel_admin_user: (id)=> urls.users.register+ '/' + id + '/cancel_admin',
        become_premium: users + '/become_premium'
    }
}

export {
    baseURL,
    urls
}
