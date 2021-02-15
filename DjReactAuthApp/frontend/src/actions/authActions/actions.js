import {
  USER_LOADED,
  USER_LOADING,
  AUTH_ERROR,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_SUCCESS,
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  CHANGE_PASSWORD,
  RESET_PASSWORD_REQUEST,
  RESET_PASSWORD,
} from "./actionTypes";
import axios from "axios";

export const loadUser = () => (dispatch) => {
  dispatch({ type: USER_LOADING });
  const token = localStorage.getItem("token");
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }
  axios
    .get("/api/users/profile/", config)
    .then((res) => {
      dispatch({
        type: USER_LOADED,
        payload: res.data,
      });
    })
    .catch((err) => {
      dispatch({
        type: AUTH_ERROR,
      });
    });
};

export const login = (email, password) => (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  const body = JSON.stringify({ email, password });

  axios
    .post("api/users/login/", body, config)
    .then((res) => {
      dispatch({
        type: LOGIN_SUCCESS,
        payload: res.data,
      });
    })
    .catch((err) => {
      console.log(err);
    });
};

export const logout = () => (dispatch) => {
  const token = localStorage.getItem("token");
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  if (token) {
    config.headers["Authorization"] = `Token ${token}`;
  }
  axios
    .post("api/users/logout/", null, config)
    .then((res) => {
      console.log(res);
      dispatch({
        type: LOGOUT_SUCCESS,
      });
    })
    .catch((err) => {
      console.log(err);
    });
};

export const passwordResetRequest = (email) => (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  const body = JSON.stringify({ email });

  axios
    .post("api/users/password-reset/", body, config)
    .then((res) => {
      dispatch({
        type: RESET_PASSWORD_REQUEST,
      });
    })
    .catch((err) => {
      console.log(err);
    });
};

export const confirmPasswordReset = (
  new_password,
  confirm_password,
  uidb64,
  token
) => (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  const body = JSON.stringify({
    new_password,
    confirm_password,
    uidb64,
    token,
  });
  console.log(body);

  axios
    .post("api/users/password-reset/confirm/", body, config)
    .then((res) => {
      dispatch({
        type: RESET_PASSWORD,
      });
    })
    .catch((err) => {
      console.log(err);
    });
};
