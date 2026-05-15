import { useState, useEffect } from "react";

import axios from "axios";

function Dashboard() {

    const [title, setTitle] = useState("");

    const [originalUrl, setOriginalUrl] = useState("");

    const [urls, setUrls] = useState([]);

    const [search, setSearch] = useState("");

    const [page, setPage] = useState(1);

    const [totalPages, setTotalPages] = useState(1);

    const [editId, setEditId] = useState(null);

    const fetchUrls = async () => {

        try {

            const response = await axios.get(
                "/api/list-urls/",
                {
                    params: {

                        user_id: localStorage.getItem("user_id"),

                        search: search,

                        page: page
                    }
                }
            );

            setUrls(response.data.data);

            setTotalPages(response.data.total_pages);

        } catch (error) {

            console.log(error);
        }
    };

    useEffect(() => {

        fetchUrls();

    }, [search, page]);

    const handleAddUrl = async (e) => {

        e.preventDefault();

        try {

            if (editId) {

                await axios.put(
                    `/api/update-url/${editId}/`,
                    {
                        title: title,
                        original_url: originalUrl
                    }
                );

                alert("URL Updated Successfully");

                setEditId(null);

            } else {

                await axios.post(
                    "/api/create-url/",
                    {
                        user_id: localStorage.getItem("user_id"),

                        title: title,

                        original_url: originalUrl
                    }
                );

                alert("URL Added Successfully");
            }

            setTitle("");

            setOriginalUrl("");

            fetchUrls();

        } catch (error) {

            console.log(error);

            if (error.response) {

                alert(error.response.data.error);

            } else {

                alert("Error");
            }
        }
    };

    const handleDelete = async (id) => {

        try {

            await axios.delete(
                `/api/delete-url/${id}/`
            );

            alert("Deleted Successfully");

            fetchUrls();

        } catch (error) {

            console.log(error);
        }
    };

    const handleEdit = (url) => {

        setEditId(url.id);

        setTitle(url.title);

        setOriginalUrl(url.original_url);
    };

    const handleLogout = () => {

        localStorage.clear();

        window.location.href = "/login";
    };

    return (

        <div className="container mt-5">

            <button
                className="btn btn-danger mb-3"
                onClick={handleLogout}
            >
                Logout
            </button>

            <h2>Dashboard</h2>

            <div className="mb-3">

                <input
                    type="text"
                    className="form-control"
                    placeholder="Search by title/url"
                    value={search}
                    onChange={(e) =>
                        setSearch(e.target.value)
                    }
                />

            </div>

            <form onSubmit={handleAddUrl}>

                <div className="mb-3">

                    <input
                        type="text"
                        className="form-control"
                        placeholder="Enter title"
                        value={title}
                        onChange={(e) =>
                            setTitle(e.target.value)
                        }
                    />

                </div>

                <div className="mb-3">

                    <input
                        type="text"
                        className="form-control"
                        placeholder="Enter URL"
                        value={originalUrl}
                        onChange={(e) =>
                            setOriginalUrl(e.target.value)
                        }
                    />

                </div>

                <button
                    type="submit"
                    className="btn btn-primary"
                >
                    {
                        editId
                            ? "Update URL"
                            : "Add URL"
                    }
                </button>

            </form>

            <hr />

            <h3>Your URLs</h3>

            <table className="table">

                <thead>

                    <tr>

                        <th>Title</th>

                        <th>Short Code</th>

                        <th>Created At</th>

                        <th>Actions</th>

                    </tr>

                </thead>

                <tbody>

                    {
                        urls.map((url) => (

                            <tr key={url.id}>

                                <td>{url.title}</td>

                                <td>{url.short_code}</td>

                                <td>{url.created_at}</td>

                                <td>

                                    <button
                                        className="btn btn-warning btn-sm me-2"
                                        onClick={() =>
                                            handleEdit(url)
                                        }
                                    >
                                        Edit
                                    </button>

                                    <button
                                        className="btn btn-danger btn-sm"
                                        onClick={() =>
                                            handleDelete(url.id)
                                        }
                                    >
                                        Delete
                                    </button>

                                </td>

                            </tr>
                        ))
                    }

                </tbody>

            </table>

            <div className="mt-3">

                <button
                    className="btn btn-secondary me-2"
                    disabled={page === 1}
                    onClick={() =>
                        setPage(page - 1)
                    }
                >
                    Previous
                </button>

                <span>
                    Page {page} of {totalPages}
                </span>

                <button
                    className="btn btn-secondary ms-2"
                    disabled={page === totalPages}
                    onClick={() =>
                        setPage(page + 1)
                    }
                >
                    Next
                </button>

            </div>

        </div>
    );
}

export default Dashboard;