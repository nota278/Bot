﻿using Interfaces;
using Octokit;
using Storage.Local;
using Storage.Remote.GitHub;

namespace Platform.Bot.Triggers
{
    using TContext = Issue;
    /// <summary>
    /// <para>
    /// Represents the hello world trigger.
    /// </para>
    /// <para></para>
    /// </summary>
    /// <seealso cref="ITrigger{TContext}"/>
    internal class HelloWorldTrigger : ITrigger<TContext>
    {
        private readonly GitHubStorage _gitHubApi;
        private readonly FileStorage _fileStorage;
        private readonly string _fileSetName;

        /// <summary>
        /// <para>
        /// Initializes a new <see cref="HelloWorldTrigger"/> instance.
        /// </para>
        /// <para></para>
        /// </summary>
        /// <param name="gitHubApi">
        /// <para>A git hub api.</para>
        /// <para></para>
        /// </param>
        /// <param name="fileStorage">
        /// <para>A file storage.</para>
        /// <para></para>
        /// </param>
        /// <param name="fileSetName">
        /// <para>A file set name.</para>
        /// <para></para>
        /// </param>
        public HelloWorldTrigger(GitHubStorage gitHubApi, FileStorage fileStorage, string fileSetName)
        {
            this._gitHubApi = gitHubApi;
            this._fileStorage = fileStorage;
            this._fileSetName = fileSetName;
        }


        /// <summary>
        /// <para>
        /// Actions the context.
        /// </para>
        /// <para></para>
        /// </summary>
        /// <param name="context">
        /// <para>The context.</para>
        /// <para></para>
        /// </param>

        public void Action(TContext context)
        {
            foreach (var file in _fileStorage.GetFilesFromSet(_fileSetName))
            {
                _gitHubApi.CreateOrUpdateFile(context.Repository.Name, context.Repository.DefaultBranch, file);
            }
            _gitHubApi.CloseIssue(context);
        }


        /// <summary>
        /// <para>
        /// Determines whether this instance condition.
        /// </para>
        /// <para></para>
        /// </summary>
        /// <param name="context">
        /// <para>The context.</para>
        /// <para></para>
        /// </param>
        /// <returns>
        /// <para>The bool</para>
        /// <para></para>
        /// </returns>
        public bool Condition(TContext context) => context.Title.ToLower() == "hello world";
    }
}
