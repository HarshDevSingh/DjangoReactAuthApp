import React, { useState } from "react";
import { connect } from "react-redux";
import { changePassword } from "../../actions/authActions/actions";

const PasswordChange = ({ changePassword }) => {
  const [formdata, setFormData] = useState({
    old_password: "",
    new_password: "",
    confirm_password: "",
  });
  const handleFormData = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setFormData({ ...formdata, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const old_password = formdata.old_password;
    const new_password = formdata.new_password;
    const confirm_password = formdata.confirm_password;
    console.log(old_password, new_password, confirm_password);
    changePassword(old_password, new_password, confirm_password);
    setFormData({
      old_password: "",
      new_password: "",
      confirm_password: "",
    });
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Old password:
          <input
            type="password"
            name="old_password"
            value={formdata.old_password}
            onChange={handleFormData}
          />
        </label>
        <label>
          New password:
          <input
            type="password"
            name="new_password"
            value={formdata.new_password}
            onChange={handleFormData}
          />
        </label>
        <label>
          Confirm Password:
          <input
            type="password"
            name="confirm_password"
            value={formdata.confirm_password}
            onChange={handleFormData}
          />
        </label>
        <button type="submit">Change Password</button>
      </form>
    </div>
  );
};

export default connect(null, { changePassword })(PasswordChange);
