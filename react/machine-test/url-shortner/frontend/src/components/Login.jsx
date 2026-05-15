import { useState } from "react";

import axios from "axios";

import { useNavigate } from "react-router-dom";

function Login() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const handleLogin = async (e) => {

        e.preventDefault();

        try {

            const response = await axios.post(
                "/api/login/",
                {
                    username,
                    password
                }
            );

            localStorage.setItem(
                "user_id",
                response.data.user_id
            );

            alert(response.data.message);

            navigate("/dashboard");

        } catch (error) {

            console.log(error);

            if (error.response) {

                alert(JSON.stringify(error.response.data));

            } else {

                alert("Login failed");
            }
        }
    };

    return (

        <div className="container mt-5">

            <h2>Login</h2>

            <form onSubmit={handleLogin}>

                <div className="mb-3">

                    <input
                        type="text"
                        className="form-control"
                        placeholder="Username"
                        value={username}
                        onChange={(e) =>
                            setUsername(e.target.value)
                        }
                    />

                </div>

                <div className="mb-3">

                    <input
                        type="password"
                        className="form-control"
                        placeholder="Password"
                        value={password}
                        onChange={(e) =>
                            setPassword(e.target.value)
                        }
                    />

                </div>

                <button
                    type="submit"
                    className="btn btn-success"
                >
                    Login
                </button>

            </form>

        </div>
    );
}

export default Login;