import React from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";

const Logout = ({ isAuthenticated }) => {
  return (
    <div>
      <p>Logged out</p>
    </div>
  );
};
const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});
export default connect(mapStateToProps)(Logout);
