var data = [];
const git_repo = (user_name) => {
  const api = `https://api.github.com/users/${user_name}/repos`;
  fetch(api)
    .then((request) => request.json())
    .then((response) => response)
    .then((repos) => {
      data = repos.map((each_response) => {
        if (each_response.fork != true) {
          git_repos_DOM(each_response);
          return each_response;
        }
        // console.log(data);
      });
    });
};
const git_repos_DOM = (repo) => {
  const created_at = new Date(repo.created_at).toDateString();
  //   created_at = created_at;
  const updated_at = new Date(repo.updated_at).toDateString();
  //   updated_at = updated_at;
  home = document.querySelector(".git_repos__list ");
  home.innerHTML += `
  <div class="git_repo">
    <h3 class="header-tertiary git_repo__project">${repo.name}</h3>
    <div class="git_repo__identity">
      <span class="get_repo__identity--author">Owner: ${repo.owner.login}</span><br />
      <span class="git_repo__identity--language">Lang: ${repo.language}</span>
    </div>
    <div class="git_repo__description">${repo.description}</div>
    <div class="git_repo__footer">
      <div class="git_repo__footer--element">
        <span>Created at</span><br /><span>${created_at}</span>
      </div>
      <div class="git_repo__footer--element">
        <span>Last update</span><br /><span>${updated_at}</span>
      </div>
      <div class="git_repo__footer--element">
        <span>Watch</span><br /><span>${repo.watchers_count}</span>
      </div>
      <div class="git_repo__footer--element">
        <span>Stars</span><br /><span>No</span>
      </div>
    </div>
  `;
};
// git_repo("Bhuwan-web");

window.onload = git_repo("Bhuwan-web");
