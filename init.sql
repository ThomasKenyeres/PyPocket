CREATE TABLE IF NOT EXISTS `Snippets`(
    snippetID INTEGER PRIMARY KEY AUTOINCREMENT,
    snippetKey VARCHAR(15),
    snippetDescription VARCHAR(100),
    snippetValue TEXT
);
