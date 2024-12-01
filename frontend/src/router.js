import {createBrowserRouter, Navigate} from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import AuthPage from "./pages/AuthPage";
import UserPage from "./pages/UserPage";
import CarPage from "./pages/CarPage";

export const router = createBrowserRouter([
    {path:'/', element:<MainLayout/>, children:[
            {index:true, element:<Navigate to={'cars'}/>},
            {path:'cars', element:<CarPage/>},
            {path:'auth', element:<AuthPage/>},
            {path:'register', element:<UserPage/>}
        ]}
])