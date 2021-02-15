import React, { Component } from "react";
import ReactDOM from "react-dom";

import Header from "./layout/Header";
import Footer from "./layout/Footer";
import MyProfile from "./User/MyProfile";
import Register from "./Auth/Register";
import Login from "./Auth/Login";
import Logout from "./Auth/Logout";
import PasswordReset from "./Auth/PasswordReset";
import PasswordResetConfirm from "./Auth/PasswordResetConfirm";

import PrivateRoute from "./commons/PrivateRoute";

import { Provider } from "react-redux";
import store from "../store";

import { loadUser } from "../actions/authActions/actions";

import {
  HashRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";

class App extends Component {
  componentDidMount() {
    store.dispatch(loadUser());
  }

  render() {
    return (
      <Provider store={store}>
        <>
          <Router>
            <Header />
            <div>
              <Switch>
                <PrivateRoute exact path="/" component={MyProfile} />
                <Route exact path="/register" component={Register} />
                <Route exact path="/login" component={Login} />
                <Route exact path="/Logout" component={Logout} />
                <Route exact path="/reset-password" component={PasswordReset} />
                <Route
                  exact
                  path="/reset-password-confirm/:uidb64/:token"
                  component={PasswordResetConfirm}
                />
              </Switch>
            </div>
            <Footer />
          </Router>
        </>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
