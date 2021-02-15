import React from "react";
import { connect } from "react-redux";

const MyProfile = ({ user }) => {
  console.log(user.id);
  return (
    <div>
      <h1>My profile page.....</h1>
      <p>{user.email}</p>
      <img
        style={{ height: "80px", width: "80px" }}
        src={user.profile.avatar}
        alt="avatar"
      />
    </div>
  );
};
const mapStateToProps = (state) => ({
  user: state.auth.user,
});
export default connect(mapStateToProps)(MyProfile);
