import React from 'react';
import {useForm} from "react-hook-form";
import {registrationService} from "../services/registrationService";

const UserPage = () => {
    const {handleSubmit, register} = useForm();
    const registration = async (user) =>{
        await registrationService.register(user)
    }

    return (
        <div>
            <form onSubmit={handleSubmit(registration)}>
                <input type="text" placeholder={'email'} {...register('email')}/>
                <input type="text" placeholder={'password'} {...register('password')}/>
                <input type="text" placeholder={'name'} {...register('profile.name')}/>
                <input type="text" placeholder={'surname'} {...register('profile.surname')}/>
                <input type="text" placeholder={'phone number'} {...register('profile.phone_number')}/>
                <button>Register</button>
            </form>

        </div>
    );
};

export default UserPage;