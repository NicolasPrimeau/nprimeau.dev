---
title: "Le mot « artel »"
date: 2026-05-28
draft: false
tags: ["systèmes distribués", "artel"]
description: "Une note sur l'origine du nom, et un fil qui relie la Russie du 19e siècle à Leslie Lamport."
---

Je lisais *La Conquête du pain* de Kropotkine quand j'ai décidé comment nommer le projet.

Le livre parle de pain, ou plutôt de qui le fait et de qui le mange, et de la question de savoir si ces deux groupes doivent vraiment être différents. La thèse de Kropotkine, c'est que la coopération n'est pas une conquête de la civilisation posée par-dessus une nature humaine compétitive. C'est l'inverse. La coopération est plus ancienne, plus durable, plus productive. L'histoire en est remplie, si on regarde les bonnes choses.

Une des choses qu'il examine, c'est l'artel.

L'artel historique était un collectif de travailleurs russes : des artisans, des pêcheurs ou des ouvriers qui s'organisaient autour d'une tâche commune, mettaient les ressources en commun, partageaient les gains et se tenaient mutuellement responsables sans contremaître au-dessus d'eux. Aucune autorité centrale. L'artel décidait par consensus ou par coutume, travaillait en parallèle et se dissolvait une fois le travail terminé. Il était robuste justement parce qu'il n'avait aucun point de défaillance unique.

Les artels étaient partout dans la Russie préindustrielle. Puis la planification centrale est arrivée, et la plupart ont disparu. Pas parce qu'ils avaient cessé de fonctionner. Parce que le système qui les a remplacés exigeait une autre forme.

---

L'article de 1978 de Leslie Lamport, « Time, Clocks, and the Ordering of Events in a Distributed System », s'ouvre sur une observation d'une simplicité trompeuse : un système distribué n'a pas d'horloge globale. Il n'existe aucune vérité commune sur le moment où une chose s'est produite. Chaque processus ne dispose que de son propre état local et des messages qu'il a reçus.

Sa réponse : les horloges logiques. Chaque processus tient un compteur. Quand un événement survient, on l'incrémente. Quand on envoie un message, on y joint son compteur. Quand on reçoit un message, on prend le maximum entre son compteur et celui de l'expéditeur, puis on incrémente. C'est toute la règle. À partir de ce minuscule protocole local, on obtient un ordonnancement global cohérent des événements, sans coordinateur.

Ce fil traverse tout ce qui a suivi : les horloges vectorielles le généralisent pour suivre la causalité entre les processus. Les protocoles de bavardage (gossip) propagent l'état par des échanges deux à deux, de sorte que l'information se diffuse dans le réseau sans qu'aucun nœud n'ait de vue d'ensemble. Les CRDT (types de données répliquées sans conflit) vont encore plus loin : on conçoit ses structures de données de façon à ce que deux répliques puissent toujours fusionner sans conflit, peu importe l'ordre. La cohérence à terme cesse d'exiger un accord à chaque instant et demande plutôt une convergence dans le temps.

Le fil conducteur est toujours le même : un comportement collectif cohérent à partir de règles locales. Aucun coordinateur requis.

Ce qui me frappe, c'est que Kropotkine faisait le même argument, à partir de l'histoire, cent ans plus tôt. Il décrivait des artels, des sociétés d'entraide et des structures de guildes, et il pointait le même principe sous-jacent : pas besoin d'autorité centrale pour obtenir un système qui fonctionne. Il faut les bonnes règles sur la façon dont les parties interagissent. Le reste émerge.

De Kropotkine à Lamport, c'est une ligne droite. L'un l'a défendu philosophiquement, l'autre l'a prouvé mathématiquement.

---

Au moment de nommer le projet, je voulais un mot qui portait cette idée. Pas « mesh », « swarm » ou « cluster ». Ce sont des mots de topologie. L'artel, lui, parlait de l'*organisation* du travail : locale, responsable, convergente, sans hiérarchie.

[Artel](https://github.com/NicolasPrimeau/artel) est une couche de coordination pour des agents IA. Chaque instance fait tourner sa propre base de données et son propre archiviste. Les instances répliquent leur mémoire partagée les unes vers les autres au moyen d'abonnements JSON Feed : aucun serveur central, aucune infrastructure partagée requise. Un agent sur une machine peut lire et écrire des mémoires qui convergent, par bavardage, vers toutes les autres instances abonnées à son flux. Le modèle de données est pensé pour les CRDT : la dernière écriture l'emporte sur chaque entrée, des pierres tombales (tombstones) pour les suppressions, des enregistrements estampillés à l'origine pour que les boucles se court-circuitent.

L'architecture reflète la philosophie parce que la philosophie est venue en premier. L'avertissement est dans le nom.
