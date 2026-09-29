<!-- SPDX-License-Identifier: Apache-2.0 -->

# Security policy

Council Lens is primarily a text/configuration Skill. It does not ship a backend, database, authentication service, API key, executable binary, browser extension, or network daemon.

## Reporting

If you find a security issue in the repository tooling or packaged Skill, open a GitHub Security Advisory when available. Do not include real credentials, private conversations, proprietary files, or personal sensitive information in a public issue.

## Trust boundaries

- The Skill may instruct ChatGPT to use files, web research, connectors or calculations when the host makes them available; those host capabilities remain governed by the host's permissions and policies.
- The repository's release QA scans common secret patterns and archive hazards, but it is not a sandbox or exhaustive malware detector.
- External links and third-party services are outside this repository's control.
- Council Lens must not claim that independent agents or professionals participated unless that execution actually occurred.

## Supported version

Security fixes target the latest tagged release.
