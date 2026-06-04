---
title: "Complémentarité"
date: 2026-06-04
draft: false
tags: ["intelligence artificielle", "informatique théorique", "philosophie"]
description: "L'IA implémente vite, vérifie mal. L'humain vérifie vite, implémente mal. Une remarque sur P contre NP avec un paramètre que la question d'origine n'a pas : qui vérifie."
---

J'ai eu cette observation en commençant à travailler avec l'IA. Ce n'est pas une thèse, c'est un cadre. Il aide à comprendre quels problèmes l'IA est faite pour résoudre, et lesquels lui échappent.

Le cadre, c'est P contre NP. Mais avec une dimension de plus.

---

La question P contre NP demande si vérifier une solution est aussi difficile que la trouver. L'exemple habituel est le sudoku : la grille est pénible à remplir, mais une fois remplie, on voit en un coup d'oeil si elle tient. Trouver est coûteux. Vérifier est bon marché. Toute la classe NP repose sur cette asymétrie.

C'est une propriété du problème. Binaire. La vérification est dans P, ou elle n'y est pas. La question ne dit rien de qui vérifie. Elle suppose un vérificateur abstrait, et la difficulté est la même pour tout le monde.

L'IA brise cette supposition. Elle ajoute un coefficient.

---

Le même contrôle ne coûte pas la même chose selon qui le fait. Ce n'est plus facile ou difficile dans l'absolu. C'est bon marché pour un humain et cher pour une machine sur ce contrôle-ci, et l'inverse sur celui-là. La complexité devient relative au vérificateur. L'agent qui vérifie est un paramètre, et c'est exactement le paramètre que P contre NP n'a pas.

Un agent IA produit cinq cents lignes de JavaScript. Les relire pour les valider est coûteux pour un humain. Mais on charge la page, on la regarde, et on voit immédiatement si le site a l'air correct. Le certificat n'est pas dans le code. Il est dans le comportement. Lire et exécuter sont deux mécanismes de vérification différents, avec deux coefficients différents. Le mécanisme fixe le coût.

---

Et ce n'est pas que l'humain vérifie pendant que la machine implémente. Ce serait trop simple.

Chacun est bon marché là où l'autre est aveugle. L'humain attrape instantanément ce qui cloche : l'intention trahie, la chose qui a l'air fausse, le détail que l'IA a manqué et qui saute aux yeux dès qu'on l'exécute. L'IA attrape ce qu'aucun humain ne verrait en regardant : le cas limite dans la quatorzième branche, l'erreur d'indice, l'exhaustif. Ce sont des régions disjointes de l'espace de vérification. Deux forces complémentaires, au sens fort du terme : aucune n'est complète seule, et c'est leur opposition même qui les fait tenir ensemble. La puissance n'est pas dans la délégation. Elle est dans l'union.

L'IA implémente vite et vérifie mal. L'humain vérifie vite et implémente mal. Ensemble, c'est phénoménal. Mais cela veut dire que la vérification est repoussée vers l'humain, sur exactement la part qu'on ne peut pas lui retirer.

---

Rien de neuf dans la direction. La technologie a toujours bougé comme ça.

On tape des chiffres dans une calculatrice, on obtient une réponse. On n'a pas besoin de savoir comment elle fonctionne. On ne vérifie pas le circuit, on regarde si le résultat a du sens. Le compilateur a fait la même chose : plus personne ne relit le code compilé, on l'exécute et les tests font la validation. Chaque étape pousse l'humain plus haut dans la pile, vers le jugement, loin de l'exécution.

L'IA est l'itération suivante. La nouveauté, c'est que la machine à implémenter est devenue générale. Elle implémente n'importe quoi. L'humain n'est donc plus poussé vers le haut dans un seul métier à la fois. Il l'est partout, en même temps. C'est pour ça que l'IA change les choses en profondeur. C'est un gain d'efficacité énorme.

Le médecin et l'avocat sont précisément ceux qu'on veut concentrer sur la lecture des données plutôt que sur la recherche de jurisprudence ou les tests fastidieux. C'est déjà le rôle du parajuriste. L'implémentation descend, le jugement monte.

---

Le cadre se brise à un endroit précis : quand l'implémentation est la valeur.

L'art n'a pas de réponse objective. Sa sortie est entièrement subjective. Pour plusieurs, l'art généré par l'IA est correct, mais peu le trouvent réellement beau. Il n'y a pas de certificat à vérifier, parce qu'il n'y a rien à vérifier contre. Et souvent l'implémentation est elle-même la sortie. Certaines oeuvres sont jugées entièrement sur la facture, pas sur le résultat. L'asymétrie disparaît. Trouver et vérifier redeviennent le même acte.

L'écriture, la musique, c'est pareil. Là où le geste est la chose, il n'y a pas de bon marché à extraire.

---

Il reste une question sous tout ça. La vérification doit s'arrêter quelque part, sur un juge de confiance. La récursion du « qui surveille les surveillants » a besoin d'un plancher. Aujourd'hui, ce plancher est humain.

Pas parce qu'on est plus intelligents. Parce que rien n'a été prouvé plus intelligent que l'humain. Pas même l'IA. Le pari de l'intelligence artificielle générale, c'est que la somme de toute la connaissance humaine finira par dépasser l'intelligence d'un spécialiste humain, grâce à des synergies entre les domaines. Peut-être. Rien ne dit que c'est vrai. Une IA peut tisser plus de liens, peut-être même inférer à partir de ces liens, mais la base de l'inférence reste le spécialiste humain. Et l'IA d'aujourd'hui est loin d'être générale.

Pour l'instant, le coefficient le plus bas sur la vérification reste humain. Ce n'est ni une alarme ni une célébration, juste une remarque curieuse sur la forme que prend la prochaine division du travail. La machine implémente. Nous vérifions. C'est le plancher, et il tient encore.
