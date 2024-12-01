import {apiService} from "./apiService";
import * as url from "node:url";
import {urls} from "../constants/urls";

const carService = {
    get_all_cars () {
        return apiService.get(urls.cars.cars)
    },
    create_car_ad(car) {
        return apiService.post(urls.cars.create_ad)
    }
}