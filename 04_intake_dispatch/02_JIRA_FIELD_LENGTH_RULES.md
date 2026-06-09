# Jira Field Length Rules

## Purpose

This file defines how Claude must write Jira-ready Hopper Clarification field text.

## Core Rule

Short Jira fields are limited to 250 characters.

When producing text for Jira fields, Claude must keep short-field outputs under 250 characters including spaces and punctuation.

## Short Fields

Treat these Hopper Clarification fields as short fields unless the Digital Lead confirms otherwise:

- Current Problem
- Current Process
- Future Requirement
- Expected Benefit
- Impacted Systems
- Department Notes

## Select / Rating Fields

Use only the configured option value for dropdown or rating fields.

Do not add explanation inside select/rating fields.

Examples:

- Why Raised? = Client / contract requirement
- Process Mapping Required? = Yes
- Operational Impact = High
- Safety Risk = Low
- Reg / Rep Risk = High
- Commercial Risk = Medium

## Long Detail Rule

If detail exceeds 250 characters, put it in one of:

- Jira comment
- attached process artefact
- linked Markdown file
- SharePoint document
- Department Notes only if the field supports long text

## Output Format Required

When writing field-ready content, Claude must separate:

1. Jira field values under 250 characters
2. Detailed notes for comment / attachment / artefact
3. Open questions
4. Next physical action

## Do Not

Do not produce long paragraph text for short Jira fields.

Do not cram process flow detail into short fields.

Do not duplicate the same long description across multiple fields.
