import React, { useState } from "react";
import { connect } from "react-redux";
import { passwordResetRequest } from "../../actions/authActions/actions";

const PasswordReset = ({ passwordResetRequest }) => {
  const [email, setEmail] = useState("");
  const handleSubmit = (e) => {
    e.preventDefault();
    passwordResetRequest(email);
    setEmail("");
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          email:
          <input
            type="email"
            placeholder="type your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <button type="submit">Reset Password</button>
      </form>
    </div>
  );
};

export default connect(null, { passwordResetRequest })(PasswordReset);
