import React from "react";
import { Link } from "react-router-dom";
import { connect } from "react-redux";
import { logout } from "../../actions/authActions/actions";

const Header = ({ isAuthenticated, logout }) => {
  return (
    <div>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          {isAuthenticated ? (
            <Link
              to="/logout"
              onClick={(e) => {
                logout();
              }}
            >
              Logout
            </Link>
          ) : (
            <Link to="/login">Login</Link>
          )}
        </li>
        <li>
          {isAuthenticated ? (
            <Link to="/change-password">Change Password</Link>
          ) : (
            <Link to="/register">Register</Link>
          )}
        </li>
      </ul>
    </div>
  );
};
const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});
export default connect(mapStateToProps, { logout })(Header);
