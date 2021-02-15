import React, { useState } from "react";
import { login } from "../../actions/authActions/actions";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import { Link } from "react-router-dom";

const Login = ({ login, isAuthenticated }) => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const handleFormData = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setFormData({ ...formData, [name]: value });
  };

  const handleOnSubmit = (e) => {
    e.preventDefault();
    login(formData.email, formData.password);
    setFormData({ email: "", password: "" });
  };
  if (isAuthenticated) {
    return <Redirect to="/" />;
  }
  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleOnSubmit}>
        <label>
          Email:
          <input
            type="email"
            name="email"
            required
            placeholder="type your email here"
            value={formData.email}
            onChange={handleFormData}
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            name="password"
            required
            placeholder="type your password"
            value={formData.password}
            onChange={handleFormData}
          />
        </label>
        <button type="submit">Login</button>
      </form>
      <Link to="/reset-password">Forgot password</Link>
    </div>
  );
};
const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});
export default connect(mapStateToProps, { login })(Login);
