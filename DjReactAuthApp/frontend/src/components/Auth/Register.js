import React, { useState } from "react";

const Register = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    password2: "",
    isError: false,
  });
  const handleFormData = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setFormData({ ...formData, [name]: value });
  };

  const handleOnSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    if (formData.password != formData.password2) {
      alert("confirm password did not match");
      setFormData({ email: "", password: "", password2: "", isError: false });
    }
    setFormData({ email: "", password: "", password2: "", isError: false });
  };
  return (
    <div>
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
        <label>
          Confirm Password:
          <input
            type="password"
            name="password2"
            required
            placeholder="confirm password"
            value={formData.password2}
            onChange={handleFormData}
          />
        </label>
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default Register;
