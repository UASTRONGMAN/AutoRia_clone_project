import React from 'react';
import {urls} from "../constants/urls";

const HeaderComponent = () => {
    return (
        <div>
            If you want to add car advertisement, you have to <a href={urls.auth.auth}>login</a>
        </div>
    );
};

export default HeaderComponent;