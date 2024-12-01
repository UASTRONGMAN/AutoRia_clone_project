import {apiService} from "./apiService";
import * as url from "node:url";

const carService = {
    get_all_cars () {
        return apiService.get(urls.cars.all_cars)
    },
    create_car_ad(car) {
        return apiService.post(urls.cars)
    }
}