import {apiService} from "./apiService";
import {urls} from "../constants/urls";

const registrationService = {
    register(user){
        return apiService.post(urls.register.register, user);
    }
}

export {registrationService}