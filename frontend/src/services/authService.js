import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const authService = {
    async auth(user){
        let {data:{access_token}} = await apiService.post(urls.auth, user);
        localStorage.setItem('access_token', access_token)
    }
}

export {authService}