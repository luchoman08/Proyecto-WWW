import api from "./api";

const create = user => {
  return api.post("user", user);
};

// todo: add pagination
const list = (page = 0) => {
  return api.get("user");
};

const del = id => {
  return api.del(`user/${id}`);
};

const get = id => {
  return api.get(`user/${id}`);
};

export default { list, del, get, create };
