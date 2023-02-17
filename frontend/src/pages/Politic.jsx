import React, { useEffect, useState } from "react";
import Blog from "../components/Blog";
import { GetContent } from "../services/GetContent";
import Loader from "../components/Loader";
import notfound from "../assets/notfound.png";
const Politic = () => {
  const [blogs, setBlogs] = useState([]);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    GetContent("politic").then((data) => {
      setBlogs(data);
      setLoading(false);
    });
  }, []);
  return (
    <div className="container">
      <div className="row">
        {loading ? (
          <Loader />
        ) : blogs.length > 0 ? (
          blogs.map((blog) => <Blog key={blog.id} blog={blog} />)
        ) : (
          <div className="col-12">
            <img src={notfound} alt="notfound" className="img-fluid" />
          </div>
        )}
      </div>
    </div>
  );
};

export default Politic;