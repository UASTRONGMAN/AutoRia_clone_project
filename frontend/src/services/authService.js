import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const authService = {
    async auth(user){
        const {data:{access}} = await apiService.post(urls.auth.auth, user);
        localStorage.setItem('access', access)
    }
}

export {authService}