import { useState } from "react";

import axios from "axios";

import { useNavigate } from "react-router-dom";

function Signup() {

    const navigate = useNavigate();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const handleSignup = async (e) => {

        e.preventDefault();

        try {

            const response = await axios.post(
                "/api/signup/",
                {
                    username,
                    password
                }
            );

            alert(response.data.message);

            navigate("/login");

        } catch (error) {

            console.log(error);

            if (error.response) {

                alert(JSON.stringify(error.response.data));

            } else {

                alert("Signup failed");
            }
        }
    };

    return (

        <div className="container mt-5">

            <h2>Signup</h2>

            <form onSubmit={handleSignup}>

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
                    className="btn btn-primary"
                >
                    Signup
                </button>

            </form>

        </div>
    );
}

export default Signup;