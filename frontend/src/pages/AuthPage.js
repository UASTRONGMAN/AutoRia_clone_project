import React from 'react';
import {useForm} from "react-hook-form";
import {authService} from "../services/authService";
import {urls} from "../constants/urls";

const AuthPage = () => {

    const {handleSubmit, register} = useForm();
    const login = async (user) =>{
        await authService.auth(user)
    }

    return (
        <div>
            <form onSubmit={handleSubmit(login)}>
                <input type="text" placeholder={'email'} {...register('email')}/>
                <input type="text" placeholder={'password'} {...register('password')}/>
                <button>login</button>
            </form>
            Don't have an account yet? <a href={urls.users.register}>Create.</a>
        </div>
    );
};

export default AuthPage;