import React from 'react';
import {useForm} from "react-hook-form";
import {authService} from "../services/authService";
import {urls} from "../constants/urls";

const UserPage = () => {
    const {handleSubmit, register} = useForm();
    const registration = async (user) =>{
        await authService.auth(user)
    }

    return (
        <div>
            <form onSubmit={handleSubmit(registration)}>
                <input type="text" placeholder={'email'} {...register('email')}/>
                <input type="text" placeholder={'password'} {...register('password')}/>
                <input type="text" placeholder={'name'} {...register('name')}/>
                <input type="text" placeholder={'surname'} {...register('surname')}/>
                <input type="text" placeholder={'phone_number'} {...register('phone_number')}/>
                <button>Register</button>
            </form>
        </div>
    );
};

export default UserPage;