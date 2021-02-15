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
} from "../../actions/authActions/actionTypes";

const initialState = {
  isAuthenticated: false,
  IsLoading: false,
  user: null,
};

const auth = (state = initialState, action) => {
  switch (action.type) {
    case USER_LOADING:
      return {
        ...state,
        IsLoading: true,
      };

    case USER_LOADED:
      return {
        ...state,
        IsLoading: false,
        isAuthenticated: true,
        user: action.payload,
      };
    case AUTH_ERROR:
      localStorage.removeItem("token");
      return {
        ...state,
        IsLoading: false,
        isAuthenticated: false,
        user: null,
      };
    case LOGIN_SUCCESS:
      localStorage.setItem("token", action.payload.token);
      return {
        ...state,
        IsLoading: false,
        isAuthenticated: true,
        user: action.payload.user,
      };
    case LOGOUT_SUCCESS:
      localStorage.removeItem("token");
      return {
        ...state,
        IsLoading: false,
        isAuthenticated: false,
        user: null,
      };
    case RESET_PASSWORD_REQUEST:
      localStorage.removeItem("token");
      return {
        ...state,
        IsLoading: false,
        isAuthenticated: false,
        user: null,
      };
    case RESET_PASSWORD:
      localStorage.removeItem("token");
      return {
        ...state,
        IsLoading: false,
        isAuthenticated: false,
        user: null,
      };
    default:
      return state;
  }
};

export default auth;
