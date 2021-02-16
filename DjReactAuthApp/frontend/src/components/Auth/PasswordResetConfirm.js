import React, { useState } from "react";
import { connect } from "react-redux";
import { confirmPasswordReset } from "../../actions/authActions/actions";

const PasswordResetConfirm = ({ confirmPasswordReset, ...props }) => {
  const uidb64 = props.match.params.uidb64;
  const token = props.match.params.token;
  const [formdata, setFormData] = useState({
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
    console.log(formdata);
    const new_password = formdata.new_password;
    const confirm_password = formdata.confirm_password;
    confirmPasswordReset(new_password, confirm_password, uidb64, token);
    setFormData({
      new_password: "",
      confirm_password: "",
    });
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
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
        <button type="submit">Reset Password</button>
      </form>
    </div>
  );
};

export default connect(null, { confirmPasswordReset })(PasswordResetConfirm);
