import React from 'react';
import {Outlet} from "react-router-dom";
import HeaderComponent from "../components/HeaderComponent";

const MainLayout = () => {
    return (
        <div>
            <Outlet/>
        </div>
    );
};

export default MainLayout;