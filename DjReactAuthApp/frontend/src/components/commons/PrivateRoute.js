import React, { useEffect } from "react";
import { Route, Redirect } from "react-router-dom";
import { connect } from "react-redux";
import { loadUser } from "../../actions/authActions/actions";

const PrivateRoute = ({ component: Component, auth, ...rest }) => {
  return (
    <Route
      {...rest}
      render={(props) => {
        if (auth.IsLoading) {
          return <h2>Loading...</h2>;
        } else if (!auth.isAuthenticated) {
          return <Redirect to="/login" />;
        } else {
          return <Component {...props} />;
        }
      }}
    />
  );
};
const mapStateToProps = (state) => ({
  auth: state.auth,
});
export default connect(mapStateToProps, { loadUser })(PrivateRoute);
