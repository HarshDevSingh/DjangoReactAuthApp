import React, { Component } from "react";
import ReactDOM from "react-dom";

import Header from "./layout/Header";
import { Provider } from "react-redux";
import store from "../store";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <>
          <Header />
          <h1>hello</h1>
        </>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
